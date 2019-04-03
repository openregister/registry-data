# -*- coding: utf-8 -*-

import requests

register_ids = [
    "allergen",
    "approved-open-standard",
    "approved-open-standard-guidance",
    "clinical-commissioning-group",
    "country",
    "datatype",
    "ddat-profession-capability-framework",
    "ddat-profession-capability-framework-job-family",
    "ddat-profession-capability-framework-level",
    "ddat-profession-capability-framework-role",
    "ddat-profession-capability-framework-role-level",
    "ddat-profession-capability-framework-skill",
    "ddat-profession-capability-framework-skill-level",
    "ddat-profession-capability-framework-skill-type",
    "field",
    "further-education-college-region-uk",
    "further-education-college-uk",
    "government-domain",
    "government-organisation",
    "government-service",
    "information-sharing-agreement-0001",
    "information-sharing-agreement-powers-and-objectives-0001",
    "information-sharing-agreement-specified-person-0001",
    "internal-drainage-board",
    "jobcentre",
    "jobcentre-district",
    "jobcentre-group",
    "local-authority-eng",
    "local-authority-nir",
    "local-authority-sct",
    "local-authority-type",
    "principal-local-authority",
    "prison-estate",
    "qualification-assessment-method",
    "qualification-level",
    "qualification-sector-subject-area",
    "qualification-type",
    "register",
    "registration-district",
    "school-type-eng",
    "statistical-geography",
    "statistical-geography-county-eng",
    "statistical-geography-local-government-district-nir",
    "statistical-geography-london-borough-eng",
    "statistical-geography-metropolitan-district-eng",
    "statistical-geography-non-metropolitan-district-eng",
    "statistical-geography-registration-district-eng",
    "statistical-geography-registration-district-wls",
    "statistical-geography-unitary-authority-eng",
    "statistical-geography-unitary-authority-wls",
    "territory",
]


def fetch_rsf(uid):
    print(f"Fetching {uid}...")
    resp = requests.get(f"https://{uid}.register.gov.uk/download-rsf")

    if resp.status_code != requests.codes.ok:
        print(f"{uid} couldn't be fetched.")
        return

    if resp.encoding is None:
        resp.encoding = 'utf-8'

    with open(f"rsf/{uid}.rsf", "w") as handle:
        handle.write(resp.text)


if __name__ == '__main__':
    for uid in register_ids:
        fetch_rsf(uid)
