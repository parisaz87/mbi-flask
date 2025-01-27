from datetime import datetime

INACTIVE = 0
NEW = 1
ACTIVE = 2

REPORTER_STATUS = {
    INACTIVE: 'inactive',
    NEW: 'new',
    ACTIVE: 'active',
}

NOT_RECORDED = -1
NONE = 0
NONURGENT = 1
CRITICAL = 2

PATHOLOGIES = (NONURGENT, CRITICAL)

CONCLUSION = {
    NONE: ("No pathology",
           ("No gross pathology that would require clinical follow up "
            "has been identified")),
    NONURGENT: ("Non-urgent pathology",
                ("Pathology that requires non-urgent clinical follow"
                 " up has been identified")),
    CRITICAL: ("Critial pathology",
               ("Pathology that requires urgent clinical follow up "
                "has been identified. The individual should be "
                "referred for follow up immediately."))
}


IGNORE = 0
LOW = 1
MEDIUM = 2
HIGH = 3

SESSION_PRIORITY = {
    IGNORE: 'Ignored',
    LOW: "Low",
    MEDIUM: "High",
    HIGH: "Urgent"
}

# The number of days between sessions before a new report is required
REPORT_INTERVAL = 365


MRI = 0
PET = 1

MODALITIES = {
    MRI: "MRI",
    PET: "PET"
}

# User roles
ADMIN_ROLE = 1
REPORTER_ROLE = 2
