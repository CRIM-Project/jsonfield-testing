$(document).ready(function() {
    $('#submit').click(function() {
        var list = ['exact', 'monnayage'];
        for (var value of list) {
            $('#container')
                .append(`<input type="checkbox" id="${value}" name="detail" value="${value}">`)
                .append(`<label for="${value}">${value}</label></div>`)
                .append(`<br>`);
        }
    })
});