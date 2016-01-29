/**
 * Created by Azad on 08-Jan-16.
 */





var base_url = 'http://'+location.host+'/api' //This is your server URL


function sentdata(button_status) {

    $.get(base_url, {value: button_status}, function (data) {
    });

}
