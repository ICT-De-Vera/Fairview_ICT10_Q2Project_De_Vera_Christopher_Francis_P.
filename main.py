from pyscript import document


PROJECTS = [
    {
        "name": "Q2 Seatwork 1",
        "category": "ICT 10 · Seatwork",
        "description": "A live web project made for my ICT 10 Q2 seatwork.",
        "live_url": "https://ict-de-vera.github.io/Fairview_ICT10_Q2Seatwork1_De_Vera_Christopher_Francis_P./",
        "source_url": "https://github.com/ICT-De-Vera/Fairview_ICT10_Q2Seatwork1_De_Vera_Christopher_Francis_P..git",
    },
    {
        "name": "Q2 Skills Test",
        "category": "ICT 10 · Skills test",
        "description": "A live web project made for my ICT 10 Q2 skills test.",
        "live_url": "https://ict-de-vera.github.io/Fairview_ICT10_Q2SkillsTest_De_Vera_Christopher_Francis_P./",
        "source_url": "https://github.com/ICT-De-Vera/Fairview_ICT10_Q2SkillsTest_De_Vera_Christopher_Francis_P..git",
    },
    {
        "name": "Q2 Drill 2",
        "category": "ICT 10 · Drill",
        "description": "A live web project made for my ICT 10 Q2 Drill 2.",
        "live_url": "https://ict-de-vera.github.io/FV_ICT10S_Q2Drill2_De_Vera_Christopher_Francis_P./",
        "source_url": "https://github.com/ICT-De-Vera/FV_ICT10S_Q2Drill2_De_Vera_Christopher_Francis_P..git",
    },
]


project_list = document.querySelector("#project-list")
project_list.replaceChildren()

if not PROJECTS:
    message = document.createElement("p")
    message.className = "col-12 text-secondary"
    message.textContent = "No projects have been added yet."
    project_list.appendChild(message)

for project in PROJECTS:
    card = document.createElement("article")
    card.className = "card project-card col-12 col-md-6 border-0 shadow-sm"

    body = document.createElement("div")
    body.className = "card-body p-4"

    category = document.createElement("p")
    category.className = "project-category text-uppercase fw-semibold mb-2"
    category.textContent = project["category"]

    title = document.createElement("h3")
    title.className = "h5 card-title"
    title.textContent = project["name"]

    description = document.createElement("p")
    description.className = "card-text text-secondary"
    description.textContent = project["description"]

    links = document.createElement("div")
    links.className = "d-flex flex-wrap gap-3 mt-3"

    live_link = document.createElement("a")
    live_link.className = "fw-semibold"
    live_link.href = project["live_url"]
    live_link.target = "_blank"
    live_link.rel = "noopener noreferrer"
    live_link.textContent = "Live site ↗"

    source_link = document.createElement("a")
    source_link.className = "fw-semibold"
    source_link.href = project["source_url"]
    source_link.target = "_blank"
    source_link.rel = "noopener noreferrer"
    source_link.textContent = "Source code ↗"

    links.appendChild(live_link)
    links.appendChild(source_link)
    body.appendChild(category)
    body.appendChild(title)
    body.appendChild(description)
    body.appendChild(links)
    card.appendChild(body)
    project_list.appendChild(card)
