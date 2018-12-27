$(window).scroll(function () {
        if ($(".navbar").offset().top > 40) {
            $(".navbar").removeClass('bg-transparent');
            $(".navbar").addClass("top-nav");
        }else {$(".fixed-top").removeClass("bg-top-nav");
        $(".fixed-top").addClass("bg-transparent")}
    });


function checkboxOnclick(checkbox) {

    if (checkbox.checked == true) {

//Action for checked
        window.location.href="/change-theme/video"

    } else {

//Action for not checked
        window.location.href="/change-theme/photo"

    }
};

function setCheckbox(now) {

    // var el = document.getElementById('bgCheck')

    if (now == 'video') {
        $("#bgCheck").attr("checked","checked");
    } else {
        $("#bgCheck").prop("checked", false);
    }
};

$(function () {

    // hide or show tag edit form
    $('#tag-btn').click(function () {
        $('#tags').hide();
        $('#tag-form').show();
    });
    $('#cancel-tag').click(function () {
        $('#tag-form').hide();
        $('#tags').show();
    });
    // hide or show description edit form
    $('#description-btn').click(function () {
        $('#description').hide();
        $('#description-form').show();
    });
    $('#cancel-description').click(function () {
        $('#description-form').hide();
        $('#description').show();
    });
    // delete confirm modal
    $('#confirm-delete').on('show.bs.modal', function (e) {
        $('.delete-form').attr('action', $(e.relatedTarget).data('href'));
    });

    $("[data-toggle='tooltip']").tooltip({title: moment($(this).data('timestamp')).format('lll')})

});


