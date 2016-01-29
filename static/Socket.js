/**
 * Created by Azad on 09-Jan-16.
 *
 *
 * ReconnectingWebSocket A custom 3rd party library
 * https://github.com/joewalnes/reconnecting-websocket.git
 *
 *
 *
 */
var url = 'ws://'+location.host+'/ws';

var ws = new ReconnectingWebSocket(url, null, {debug: true, reconnectInterval: 3000});
var $message = $('#message');

ws.onopen = function () {
    $message.attr("class", 'label label-success');
    $message.text('open');
};
ws.onmessage = function (ev) {

    $message.attr("class", 'label label-info');
    $message.hide();
    $message.fadeIn("slow");
    $message.text('recieved message');

    var json = JSON.parse(ev.data);

    var button_ststus = json.value;

    $(".switch").each(function (index) {

        $(this).bootstrapToggle(button_ststus[index] == '1' ? 'on' : 'off');
    });
};
ws.onclose = function (ev) {

    console.log('clode');
    $message.attr("class", 'label label-danger');
    $message.text('closed');
};
ws.onerror = function (ev) {
    $message.attr("class", 'label label-warning');
    $message.text('Error occurred, try to reconnect');
};