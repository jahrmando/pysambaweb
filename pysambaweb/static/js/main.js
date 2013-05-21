$(document).ready(function() {

    if( ($('#language').val()).indexOf("es") !== -1 ){
        $._.setLocale('es');
    }

    jQuery.validator.addMethod(
        "textOnly", 
        function(value, element) { return /^[a-zA-Z0-9_]+$/.test(value); }, 
        $._("Field alphanumeric and symbols _")
        );
    jQuery.validator.addMethod(
        "notEqual",
        function(value, element, params) {
            if ( value == $(params).val() ) { return false; 
            } else{ return true; };
        },
        $._("Your new password has not changed")
        );

    $('#formpasswd').validate({
        rules: {
            nickname: {
                required : true,
                minlength: 2,
                textOnly : true
            },
            oldpasswd: {
                required : true,
                minlength: 10,
                textOnly : true
            },
            newpasswd: {
                required : true,
                minlength: 10,
                textOnly : true,
                notEqual : '#oldpasswd'
            },
            retpasswd: {
                required : true,
                minlength: 10,
                textOnly : true,
                equalTo : '#newpasswd'
            }
        },
        messages: {
            nickname: {
                required: $._("This field is required"),
                minlength: $._("{0} Minimum  characters")
            },
            oldpasswd: {
                required: $._("This field is required"),
                minlength: $._("{0} Minimum  characters")
            },
            newpasswd: {
                required: $._("This field is required"),
                minlength: $._("{0} Minimum  characters")
            },
            retpasswd: {
                required: $._("This field is required"),
                minlength: $._("{0} Minimum  characters"),
                equalTo: $._("Confirm your new password")
            }
        },
        highlight: function(element) {
            $(element).closest('.control-group')
            .removeClass('success').addClass('error');
        },
        success: function(element) {
            $(element)
            .text('OK!').addClass('valid')
            .closest('.control-group').removeClass('error')
            .addClass('success').removeClass('fail');
        }
    });
});