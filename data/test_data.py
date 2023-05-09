

class TestData:
    # for Suite 2. Test text-box submit form on "text_box" page, "test_url_box"
    # for Suite 2. Test text-box submit form on "text_box" page, "test_box_output"
    data_text_box = [
        "Khazimat Semere", "xejok61334@duiter.com", "4573 Metz Lane, UNITED STATES", "42213 Paramount Lane, Canada"]

    # for Suite 5. Test Web Tables, "test_webtable_add_row"
    data_add_row_table = ["Test_add_first_name", "Test_add_last_name", "add_xejok61334@duiter.com", "1", "1",
                          "Test_add_department"]

    # for Suite 5. Test Web Tables, "test_webtable_edit_row"
    # for Suite 5. Test Web Tables, "test_webtable_delete_row"
    data_edit_row_table = ["Test_edit_first_name", "Test_edit_last_name", "edit_xejok61334@duiter.com", "2", "2",
                           "Test_edit_department"]

    # for Suite 7. Test Links, "test_api_call_link"
    expected_status_respond = ["201", "204", "301", "400", "401", "403", "404"]

    # conftest.py, "setup"
    # for Suite 9. Test File Transfer, "test_download"
    # for Suite 9. Test File Transfer, "test_upload"
    download_directory = "C:\\Users\\bogod\\PycharmProjects\\pythonProject\\WebInteractionDemoQA\\data\\"
    file_name = "sampleFile.jpeg"

    # for Suite 10. Test Dynamic Properties, "test_button_color_change"
    expected_white = "rgba(255, 255, 255, 1)"
    expected_red = "rgba(220, 53, 69, 1)"

    # for Suite 11. Test Forms
    data_forms = {"first_name": "Semere", "last_name": "Khazimat", "email": "xejok61334@duiter.com", "gender": "Female",
                  "mobile": "5720001111", "month_birth": "June", "month_birth_assert": "Jun", "year_birth": "1990",
                  "day_birth": "15", "hobby_1": "Sports", "hobby_2": "Music", "subject_short": "co",
                  "subject_full": "Commerce", "address": "42213 Paramount Lane", "state": "NCR", "city": "Noida",
                  "success_message": "Thanks for submitting the form"}



