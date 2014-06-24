/**
 * Created by astyfx
 */

$(document).ready(function () {
    $.getCsrfToken = function () {
        // Extract CSRF token from cookies
        var cookies = document.cookie.split(';');
        var csrf_token = null;
        $.each(cookies, function (index, cookie) {
            cookieParts = $.trim(cookie).split('=');
            if (cookieParts[0] == 'csrftoken') {
                csrfToken = cookieParts[1];
            }
        });
        return csrfToken;
    };

    $.postJSON = function (url, data, success, done) {
        return $.ajax({
            type: 'POST',
//            beforeSend: function (xhr, settings) {
//                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//                    // Only send the token to relative URLs i.e. locally.
//                    xhr.setRequestHeader("X-CSRFToken", $.getCsrfToken());
//                }
//            },
            url: url,
            data: data,
            success: success,
            complete: function () {
            },
            dataType: 'json',
            contentType: "application/json; charset=UTF-8"
        });
    };


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


    $('#caTestForm').on('submit', function () {
        event.preventDefault();
        var jsonData = new Object();
        jsonData.message = 'test';
        jsonData = JSON.stringify(jsonData);
        $.postJSON('/send_message', jsonData, function (result) {
            console.log(result);
        });
    });
});