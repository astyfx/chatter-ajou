/**
 * Created by astyfx
 */

$(document).ready(function () {

    Pusher.log = function (message) {
        if (window.console && window.console.log) {
            window.console.log(message);
        }
    };

    var pusher = new Pusher('1c903b586c466374d972');
    var channel = pusher.subscribe('test_channel');
    channel.bind('test_event', function (data) {
        alert(data.message);
    });
});