
function GetTableItemList(element){

    //window.location = $(this).data("href");
    var urlel = element.getAttribute('data-url');
    floatingsearch   = $("#floatingSearch").val();
    floatingCategory = $("#floatingCategory").val();


    $.ajax({
        url: urlel  ,
        type: 'GET',
        data: {
            'search'           :floatingsearch,
            'category'         :floatingCategory,
            // 'csrfmiddlewaretoken'   : csrftoken
        },
        dataType: "json",
    
        success : function (resp) {
            // console.log(resp);
            $(".tablelist").html(resp.html);
        },
        error: function(){

        }
    });
}


function GetTotalRatesValue(){
    var totalratesWeekdays = parseInt ($("#inpsubwdays").val());
    var totalratesWeekends = parseInt ($("#inpsubwends").val());
    var totroomwdays       = parseInt ($("#totroomwdays").val());
    var totroomwends       = parseInt ($("#totroomwends").val()) ;

    $("#totratWdays").html( (totalratesWeekdays + totroomwdays) ) ;
    $("#totratWends").html( (totalratesWeekends + totroomwends) );

}

function AddDetailitemsPack(idtm){
    data_url =  '/himitsu/packages/detail_item/add'

    var qtyval = $("#qty-"+idtm).val();
    var pid = $("#packid").val();

    $.ajax({
        url: data_url  ,
        type: 'GET',
        data: {
            'qty'    :qtyval,
            'idtm'   :idtm,
            'pid'    :pid,
            // 'csrfmiddlewaretoken'   : csrftoken
        },
        dataType: "json",
    
        success : function (resp) {
            $("#itemstable").html(resp.html);
            $("#inpsubwdays").val(resp.subweekdays);
            $("#inpsubwends").val(resp.subweekends);
            GetTotalRatesValue();
        },
        error: function(){

        }
    });

}


function UpdateDetailItemRates(element,id){

    var urlel = element.getAttribute('data-url');
    $.ajax({
      url: urlel,
      type: 'GET',
      data: {
        'qtyrates': $('#qtyrates-'+id).val(),
      },
      dataType: "json",
      success: function (resp) {
        if (resp.status) {
          location.reload();
        } else {
          alert('Data Gagal Di Ubah');
        }
      },
      error: function () {

      }
    });
 }



function GetTableRoomList(element){

    //window.location = $(this).data("href");
    var urlel = element.getAttribute('data-url');
    floatingsearch   = $("#floatingSearchRoom").val();
    floatingCategory = $("#floatingCategoryRoom").val();


    $.ajax({
        url: urlel  ,
        type: 'GET',
        data: {
            'search'           :floatingsearch,
            'category'         :floatingCategory,
            // 'csrfmiddlewaretoken'   : csrftoken
        },
        dataType: "json",
    
        success : function (resp) {
            // console.log(resp);
            $(".tableroomlist").html(resp.html);
        },
        error: function(){

        }
    });
}


function AddDetailroomsPack(idrm){
    data_url =  '/himitsu/packages/detail_room/add'

    var pid = $("#packid").val();

    $.ajax({
        url: data_url  ,
        type: 'GET',
        data: {
            'idrm'   :idrm,
            'pid'    :pid,
            // 'csrfmiddlewaretoken'   : csrftoken
        },
        dataType: "json",
    
        success : function (resp) {
            $("#roomstable").html(resp.html);
            $("#totroomwdays").val(resp.roomweekdays);
            $("#totroomwends").val(resp.roomweekends);
            GetTotalRatesValue();
        },
        error: function(){

        }
    });

}