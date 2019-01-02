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
    var flash = null;

    // 自定义一个toast函数，用来显示弹窗
    function toast(body) {
        clearTimeout(flash);
        var $toast = $('#toast');
        $toast.text(body).fadeIn();
        flash = setTimeout(function () {
            $toast.fadeOut();
        }, 3000);
    }

    var hover_timer = null;

    function show_profile_popover(e) {
        var $el = $(e.target);

        hover_timer = setTimeout(function () {
            hover_timer = null;
            $.ajax({
                type: 'GET',
                url: $el.data('href'),
                success: function (data) {
                    $el.popover({
                        html: true,
                        content: data,
                        trigger: 'manual',
                        animation: false
                    });
                    $el.popover('show');
                    $('.popover').on('mouseleave', function () {
                        setTimeout(function () {
                            $el.popover('hide');
                        }, 200);
                    });
                },
                error: function (error) {
                    toast('Server error, please try again later.');
                }
            });
        }, 500);
    }

    function hide_profile_popover(e) {
        var $el = $(e.target);

        if (hover_timer) {
            clearTimeout(hover_timer);
            hover_timer = null;
        } else {
            setTimeout(function () {
                if (!$('.popover:hover').length) {
                    $el.popover('hide');
                }
            }, 200);
        }
    }

    // 事件绑定
    $('.profile-popover').hover(show_profile_popover.bind(this), hide_profile_popover.bind(this));

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





