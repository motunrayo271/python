def main_menu(): 
    menu = """
         1 -> phone_book
         2 -> messages
         3 -> chat
         4 -> call_register
         5 -> tones
         6 -> settings
         7 -> call_divert
         8 -> music
         9 -> games
         10 -> calculator
         11 -> reminders
         12 -> clock
         13 -> profiles
         14 -> services
         15 -> sim_services
         16 -> exit
      """
    print(menu)
    menu_input = input("Pick your choice: ")
    match(menu_input):
        case "1":phone_book()



def phone_book():
	phone_book_functions = """
		1 -> search
		2 -> service_numbers
		3 -> add_name
		4 -> erase
		5 -> edit
		6 -> copy
		7 -> assign_tone
		8 -> send_b_card
		9 -> options
		10 -> speed_dials
		11 -> voice_tags
		0 -> go_back_to_main_menu
	"""
	print(phone_book_functions)
	phone_book_input = input("Pick your choice")
	match(phone_book_input):
		case "1":print("search")
		case "2":print("service_numbers")
		case "3":print("add_name")
		case "4":print("erase")
		case "5":print("edit")
		case "6":print("copy")
		case "7":print("assign_tone")
		case "8":print("send_b_card")
		case "9":options()
		case "10":print("speed_dials")
		case "11":print("voice_tags")
		 
def options():
        option_menu = """
        1 -> memory_in_use
        2 -> type_of_view
        3 -> memory status
	 """
	print(option_menu)
	options = input("pick any of your choice")
	match(options):
		case "1":print(" Memory in use")
		case "2":print("Type of view")
		case "3":print("Memory status")



main_menu()
