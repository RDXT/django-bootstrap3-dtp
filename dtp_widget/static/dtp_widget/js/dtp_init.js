$(function () {
    $('[data-dtp]').each(function (index, el) {
        var dtpOptions = {};
        var attributes = $(el)[0].attributes;
        $.each(attributes, function (index, attr) {
            if (attr.name.startsWith("dtp-")) {
                var dtpKey = attr.name.replace("dtp-", "");
                dtpKey = dtpKey.replace(/-([a-z])/g, function (m, w) {
                    return w.toUpperCase();
                });
                var value = $.isNumeric(attr.value) ? parseInt(attr.value) : attr.value;
                value = (value == "True") ? true : value;
                value = (value == "False") ? false : value;

                var accepted = ["onRenderYear", "onRenderMonth", "onRenderDay", "onRenderHour", "onRenderMinute"];

                if (accepted.includes(dtpKey)) {
                    value = eval(value);
                    if (value == undefined) {
                        console.warn("Function not defined: " + attr.value);
                    }
                }
                dtpOptions[dtpKey] = value;
            }
        });
        $(el).datetimepicker(dtpOptions);
    });
});