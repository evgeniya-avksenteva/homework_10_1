from src.widget import get_date, mask_account_card


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))

from src.processing import data_list, filter_by_state, sort_by_date

print(filter_by_state(data_list))
print(sort_by_date(data_list))
