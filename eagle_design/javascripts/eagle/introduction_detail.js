// From http://brack3t.com/ajax-and-django-views.html
// and http://stackoverflow.com/questions/1184624/convert-form-data-to-js-object-with-jquery

function apply_form_field_error(fieldname, error) {
    var input = $("#id_" + fieldname),
        container = $("#div_id_" + fieldname),
        error_msg = $("<span />").addClass("help-inline ajax-error").text(error[0]);

    container.addClass("error");
    // Is this the zurb way of doing things
    error_msg.insertAfter(input);
}

function clear_form_field_errors(form) {
    $(".ajax-error", $(form)).remove();
    $(".error", $(form)).removeClass("error");
}

// Make this a zurb modal
function django_message(msg, level) {
    var levels = {
        warning: 'alert',
        error: 'error',
        success: 'success',
        info: 'info'
    },
    source = $('#message_template').html(),
    template = Handlebars.compile(source),
    context = {
        'tags': levels[level],
        'message': msg
    },
    html = template(context);

    $("#message_area").append(html);
}

// Make this a zurb modal
function django_block_message(msg, level) {
    var source = $("#message_block_template").html(),
        template = Handlebars.compile(source),
        context = {level: level, body: msg},
        html = template(context);

    $("#message_area").append(html);
}

$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

$(document).on("submit", "form.ajaxy", function(e) {
    e.preventDefault();
    var self = $(this),
        url = self.attr("action"),
        ajax_req = $.ajax({
            url: url,
            type: "POST",
            data: self.serializeObject(),
            success: function(data, textStatus, jqXHR) {
                //django_message("saved successfully.", "success");
                console.log("saved successfully.", "success");
                $('#add_introducee_modal').foundation('reveal', 'close');
            },
            error: function(data, textStatus, jqXHR) {
                var errors = $.parseJSON(data.responseText);
                $.each(errors, function(index, value) {
                    if (index === "__all__") {
                        //django_message(value[0], "error");
                        console.log(value[0], "error");
                    } else {
                        //apply_form_field_error(index, value);
                        console.log(index, value);
                    }
                });
            }
        });
});

$(document).on("click", "a.addintroducee", function(e) {
    e.preventDefault();
    var self = $(this);
    $('input#intro_sequence').val(self.attr("data-introduction-sequence"));
    $('#add_introducee_modal').foundation('reveal', 'open');
});
