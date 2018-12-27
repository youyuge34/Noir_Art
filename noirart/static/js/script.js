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


