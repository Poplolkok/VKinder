# tokens to get access
GROUP_TOKEN = ""
USER_TOKEN = ""

# covert status to int and back
status_to_int = {
    "Не указано": 0,
    "Не женат / не замужем": 1,
    "Встречается": 2,
    "Помолвлен(-а)": 3,
    "Женат / замужем": 4,
    "Всё сложно": 5,
    "В активном поиске": 6,
    "Влюблён(-а)": 7,
    "В гражданском браке": 8
}

int_to_status = {
    0: "Не указано",
    1: "Не женат / не замужем",
    2: "Встречается",
    3: "Помолвлен(-а)",
    4: "Женат / замужем",
    5: "Всё сложно",
    6: "В активном поиске",
    7: "Влюблён(-а)",
    8: "В гражданском браке"
}