import eel
import desktop
import rakuten_api


app_name="web"
end_point="index.html"
size=(600,700)

@ eel.expose
def rakuten_system(kw_search, csv_name, box_name, select_api):
    output_data = rakuten_api.main(kw_search, csv_name, box_name, select_api)
    return output_data


desktop.start(app_name,end_point,size)