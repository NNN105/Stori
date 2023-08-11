
import time

def test_02_suggestion_class(home):
    # In the Suggestion Class Example, enter the word “Me” and select Mexico.       
    message = 'Mexico'
    home.verify_header()
    assert home.select_sugg_class() == message
    time.sleep(2) # Only for visibility
    
def test_03_dropdown(home):
    #In the Dropdown Example, select option 2 and then option 3. The user should be able to see the change
    message = 'Option2'
    home.verify_header()
    # Verify the read text is 'Option3'
    assert home.select_dropdown_OP2() == message
    time.sleep(2) # Only for visibility
    message = 'Option3'
    # Verify the read text is 'Option3'
    assert home.select_dropdown_OP3() == message
    time.sleep(2) # Only for visibility
    
def test_04_switch_windows(home):
    #In the Switch Window Example, click the Open Window button. If the 30 day money back
    #guarantee text (example below) is not shown, fail the test. Close the new window.
    message = '30 DAY MONEY BACK GUARANTEE'
    home.verify_header()
    academy = home.go_academy('window')
    # Verify the read text is '30 DAY MONEY BACK GUARANTEE'
    assert academy.check_guarantee_title() == message
    home.driver.switch_to.window(home.driver.window_handles[0]) 
    time.sleep(2) # Only for visibility
    
def test_05_switch_tab(home):
    #In the Switch Tab Example, click the Open Tab button. Scroll on the new tab until you
    #see the button below. Then take a screenshot that includes the button
    home.verify_header()
    academy = home.go_academy('tab')
    # Verify that the screenshot is taken
    assert academy.check_image() == True
    time.sleep(2) # Only for visibility

def test_06_switch_Alert(home):
    # In the Switch To Alert Example, type this string “Stori Card” and click the Alert button. Print the text in the 
    # alert and click on OK. Then type the same string and click on the Confirm button and print the text
    home.verify_header()
    # Generate an alert pressing Alert Button
    message = "Hello Stori Card, Are you sure you want to confirm?"
    alert_msg = home.select_alert("Stori Card", 'alert') 
    time.sleep(1) # Only for visibility
    assert "Stori Card" in alert_msg
    home.alert.accept()
    # Generate an alert pressing Confirm Button
    confirm_msg = home.select_alert("Stori Card", 'confirm')
    home.alert.accept()
    # Verify both messages are equal
    assert confirm_msg == message
    time.sleep(2) # Only for visibility

def test_07_web_table(home):
    #In the Web Table Example, print the number of courses that are $25. Then print their course names.
    value = 25
    qty = -1
    home.verify_header()
    # Check the number of $25 course.
    assert home.count_course(value) != qty
    time.sleep(2) # Only for visibility
    
 
def test_08_fixed_table(home):
    # Print the names of all the Engineers in the Web Table Fixed header
    value = 'engineer'
    qty = -1
    home.verify_header()
    # Verify 0 or more engineers
    assert home.count_engineer(value) != qty
    time.sleep(2) # Only for visibility
    
def test_09_iframe(home):       
    #In the iFrame example, get the text highlighted in blue in the following image and print it
    message = "His mentorship program is most after in the software testing community with long waiting period."
    home.verify_header()
    # Verify the correct message
    assert home.print_iframe() == message
    time.sleep(2) # Only for visibility  
    
