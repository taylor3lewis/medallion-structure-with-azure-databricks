from dotenv import load_dotenv

from data.skills import *
from utils.utils import get_env

load_dotenv()

import json
import random
import uuid
from copy import deepcopy

SAMPLE_FOLDER = target_filename = get_env("SAMPLE_FOLDER")


def maybe(prob: float) -> bool:
    return random.random() < prob


def noisy_text(value: str) -> str:
    options = [
        value,
        value.lower(),
        value.upper(),
        value.title(),
        f" {value}",
        f"{value} ",
        f"  {value}  ",
    ]
    return random.choice(options)


def normalize_base_job_title(title: str) -> str:
    for canonical, aliases in job_title_aliases.items():
        if title == canonical or title in aliases:
            return canonical
    return title


def sample_job_title() -> str:
    canonical = random.choice(job_titles)
    aliases = job_title_aliases.get(canonical, [canonical])
    chosen = random.choice(aliases) if maybe(0.30) else canonical
    return noisy_text(chosen) if maybe(0.20) else chosen


def sample_company() -> str | None:
    company = random.choice(companies)
    if maybe(0.08):
        return None
    if maybe(0.20):
        return noisy_text(company)
    return company


def sample_location() -> str | None:
    canonical = random.choice(locations)
    aliases = location_aliases.get(canonical, [canonical])
    chosen = random.choice(aliases) if maybe(0.35) else canonical

    if maybe(0.06):
        return None
    if maybe(0.08):
        return ""
    return chosen


def sample_salary():
    base = random.randint(3000, 25000)

    options = [
        base,
        str(base),
        f"R$ {base}",
        f"R$ {base:,.0f}".replace(",", "."),
        f"{base} BRL",
        f"{max(1000, base - 2000)}-{base + 2000}",
        f"{max(1000, base - 2000)}k-{(base + 2000) // 1000}k",
        None,
        0,
        -random.randint(1000, 5000),
    ]

    weights = [0.45, 0.10, 0.10, 0.05, 0.05, 0.10, 0.03, 0.05, 0.04, 0.03]
    return random.choices(options, weights=weights, k=1)[0]


def sample_skills() -> list:
    size = random.randint(4, 10)
    base_skills = random.sample(skills_pool, k=size)

    result = []
    for skill in base_skills:
        aliases = skill_aliases.get(skill, [skill])
        chosen = random.choice(aliases) if maybe(0.35) else skill

        if isinstance(chosen, str) and maybe(0.20):
            chosen = noisy_text(chosen)

        result.append(chosen)

        if maybe(0.12):
            result.append(chosen)

    if maybe(0.20):
        result.append(random.choice(extra_noise_skills))
    if maybe(0.10):
        result.append("")
    if maybe(0.06):
        return None

    random.shuffle(result)
    return result


def infer_description(title: str, skills: list | None) -> str | None:
    if maybe(0.10):
        return None

    skill_text = ""
    if skills:
        valid_skills = [str(s).strip() for s in skills if s not in [None, ""]]
        skill_text = ", ".join(valid_skills[:6])

    descriptions = [
        f"We are hiring a {title} to work with {skill_text}.",
        f"Opportunity for {title}. Required skills: {skill_text}.",
        f"Looking for a professional with experience in {skill_text}.",
        f"{title} role focused on cloud, data and analytics.",
        None if maybe(0.05) else f"{title} position in a modern data platform team using {skill_text}."
    ]
    return random.choice(descriptions)


def sample_employment_type():
    return random.choice(["CLT", "PJ", "Contract", "Full-time", "Hybrid"])


def generate_job() -> dict:
    title = sample_job_title()
    company = sample_company()
    location = sample_location()
    salary = sample_salary()
    skills = sample_skills()

    record = {
        "source_job_id": str(uuid.uuid4()) if maybe(0.85) else None,
        "job_title": title,
        "company": company,
        "location": location,
        "salary": salary,
        "skills": skills,
        "employment_type": sample_employment_type() if maybe(0.85) else None,
        "description": infer_description(title, skills),
        "posted_at": f"2026-04-{random.randint(1, 8):02d}T{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:00Z",
        "source": random.choice(["linkedin", "gupy", "indeed", "programathor", "synthetic_generator"]),
    }

    if maybe(0.05):
        record["job_title"] = None
    if maybe(0.04):
        record["company"] = ""
    if maybe(0.03):
        record["unexpected_field"] = random.choice(["legacy", 123, True, {"note": "extra"}])

    return record


def make_near_duplicate(record: dict) -> dict:
    dup = deepcopy(record)

    if isinstance(dup.get("job_title"), str) and maybe(0.60):
        dup["job_title"] = noisy_text(dup["job_title"])

    if isinstance(dup.get("company"), str) and maybe(0.50):
        dup["company"] = noisy_text(dup["company"])

    if isinstance(dup.get("location"), str) and maybe(0.50):
        dup["location"] = noisy_text(dup["location"])

    if isinstance(dup.get("skills"), list) and dup["skills"]:
        if maybe(0.50):
            dup["skills"].append(random.choice(dup["skills"]))
        if maybe(0.30):
            random.shuffle(dup["skills"])

    if maybe(0.40):
        dup["source_job_id"] = record.get("source_job_id")

    return dup


def generate_dataset(n=300, duplicate_rate=0.08):
    jobs = [generate_job() for _ in range(n)]

    duplicates_count = max(1, int(n * duplicate_rate))
    duplicate_indexes = random.sample(range(n), k=duplicates_count)

    for idx in duplicate_indexes:
        jobs.append(make_near_duplicate(jobs[idx]))

    random.shuffle(jobs)
    return jobs


if __name__ == "__main__":
    for i in range(1, 7):
        jobs = generate_dataset(n=50, duplicate_rate=0.08)

        with open(f"../{SAMPLE_FOLDER}jobs_raw_{i}.json", "w", encoding="utf-8") as f:
            json.dump(jobs, f, ensure_ascii=False, indent=2)

        print(f"Arquivo jobs_raw.json gerado com {len(jobs)} registros.")
