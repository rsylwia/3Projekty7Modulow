import datetime
import calendar


def translate_to_polish(day_names):
    match day_names:
        case 'Monday':
            return 'Poniedziałek'
        case 'Tuesday':
            return 'Wtorek'
        case 'Wednesday':
            return 'Środa'
        case 'Thursday':
            return 'Czwartek'
        case 'Friday':
            return 'Piątek'
        case 'Saturday':
            return 'Sobota'
        case 'Sunday':
            return 'Niedziela'


def translate_to_polish_2_way(day_names):
    english_to_polish_day_name = {
        'Monday': 'Poniedziałek',
        'Tuesday': 'Wtorek',
        'Wednesday': 'Środa',
        'Thursday': 'Czwartek',
        'Friday': 'Piątek',
        'Saturday': 'Sobota',
        'Sunday': 'Niedziela'
    }
    return english_to_polish_day_name[day_names]


date_of_bird = input("Podaj datę urodzin w formacie dzień-miesiąc-rok (np.1-1-2000): ")
day, month, year = date_of_bird.split("-")  # (1,1,2000)

date_of_bird = datetime.datetime(int(year), int(month), int(day))

day_name = calendar.day_name[date_of_bird.weekday()]
print(translate_to_polish(day_name))
print(translate_to_polish_2_way(day_name))
