from copy import deepcopy
from typing import Dict, List, Optional

# Для розв'язання цієї задачі можна використовувати шаблон "Будівельник" (Builder pattern).
# Цей шаблон дозволяє побудувати об')єкт поетапно, дозволяючи створювати профіль користувача із різними
# характеристиками за допомогою окремих будівельників, а також дозволяє керувати відсутніми даними у профілі.
class UserProfile:
    def __init__(self, name: str, education: Optional[Dict[str, str]] = None,
                 work_experience: Optional[List[Dict[str, str]]] = None,
                 technologies: Optional[List[str]] = None, photo: Optional[str] = None):
        self.name = name
        self.education = education if education else {}
        self.work_experience = work_experience if work_experience else []
        self.technologies = technologies if technologies else []
        self.photo = photo

    def __str__(self) -> str:
        return (f"Name: {self.name}\nEducation: {self.education}\n"
                f"Work Experience: {self.work_experience}\nTechnologies: {self.technologies}\n"
                f"Photo: {self.photo}")


class UserProfileBuilder:
    def __init__(self, name: str):
        self.user_profile = UserProfile(name)

    def add_education(self, education: Dict[str, str]) -> 'UserProfileBuilder':
        self.user_profile.education = education
        return self

    def add_work_experience(self, work_experience: List[Dict[str, str]]) -> 'UserProfileBuilder':
        self.user_profile.work_experience = work_experience
        return self

    def add_technologies(self, technologies: List[str]) -> 'UserProfileBuilder':
        self.user_profile.technologies = technologies
        return self

    def add_photo(self, photo: str) -> 'UserProfileBuilder':
        self.user_profile.photo = photo
        return self

    def build(self) -> UserProfile:
        return self.user_profile


# Створення профілю молодого спеціаліста
young_professional = UserProfileBuilder("Молодий Спеціаліст") \
    .add_education({"ЗВО": "ВНЗ XYZ", "Спеціальність": "ІТ", "Рік випуску": 2023}) \
    .add_technologies(["Python"]) \
    .add_photo("фото_молодого_спеціаліста.jpg") \
    .build()

# Створення профілю досвідченого сеньйора
senior_professional = UserProfileBuilder("Досвідчений Сеньйор") \
    .add_education({"ЗВО": "ВНЗ ABC", "Спеціальність": "Комп'ютерні науки", "Рік випуску": 2008,
                    "Друга вища освіта": "ВНЗ DEF", "Спеціальність": "Менеджмент", "Рік випуску": 2012}) \
    .add_work_experience([{"Компанія": "Company A", "Посада": "Розробник", "Рік початку": 2008, "Рік звільнення": 2012},
                          {"Компанія": "Company B", "Посада": "Архітектор", "Рік початку": 2012,
                           "Рік звільнення": 2022}]) \
    .add_technologies(["Java", "C#", "JavaScript", "SQL", "Docker", "AWS", "React"]) \
    .build()

print(young_professional)
print(senior_professional)
