function getStates(countryid) {
    let $ = window.jQuery;
    $.get('/location/states/' + countryid, function (resp){
        let state_list = '<option value="0" selected="">---------</option>'
        $.each(resp.data, function(i, item){
            state_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#stateid').html(state_list);

        // $('#id_kabupaten.selectpicker').selectpicker('render');
        // $('#stateid.selectpicker').selectpicker('destroy');
        // $('#stateid.selectpicker').attr( 'data-live-search','true');
        // $('#stateid.selectpicker').attr( 'data-size','8');
        // $('#stateid').addClass( 'selectpicker dropup');
        // $('#stateid.selectpicker').selectpicker('render');
    });
}

function getCities(stateid) {
    let $ = window.jQuery;
    $.get('/location/cities/' + stateid, function (resp){
        let city_list = '<option value="0" selected="">---------</option>'
        $.each(resp.data, function(i, item){
            city_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#cityid').html(city_list);

        // $('#cityid.selectpicker').selectpicker('destroy');
        // $('#cityid.selectpicker').attr( 'data-live-search','true');
        // $('#cityid.selectpicker').attr( 'data-size','8');
        // $('#cityid').addClass( 'selectpicker dropup');
        // $('#cityid.selectpicker').selectpicker('render');
    });
}

function getKelurahan(kecamatan_id) {
    let $ = window.jQuery;
    $.get('/wilayah_indonesia/kelurahan/' + kecamatan_id, function (resp){
        let kelurahan_list = '<option value="0" selected="">---------</option>'
        $.each(resp.data, function(i, item){
           kelurahan_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
        });
        $('#id_kelurahan').html(kelurahan_list);


        $('#id_kelurahan.selectpicker').selectpicker('destroy');
        $('#id_kelurahan.selectpicker').attr( 'data-live-search','true');
        $('#id_kelurahan.selectpicker').attr( 'data-size','8');
        $('#id_kelurahan').addClass( 'selectpicker dropup');
        $('#id_kelurahan.selectpicker').selectpicker('render');
    });
}


function SetStateUpdate(countryid, stateselected){
    $.ajax({
        url: '/location/states/' + countryid,
        type: 'GET',
        dataType: "text",
    
        success : function (resp) {

            let state_list = '<option value="0" selected="">---------</option>'
            respon = JSON.parse(resp);
            $.each(respon.data, function(i, item){

                if (stateselected == item.id){
                    state_list += '<option value="'+ item.id +'" selected>'+ item.name +'</option>'
                } else {
                    state_list += '<option value="'+ item.id +'">'+ item.name +'</option>'
                }
            });


            $('#stateid').html(state_list);
           
        },
        error: function(){
            console.log("error");
            // $('.header-data').html("");
            // $('.header-option').html("");
            // $('.body-item').html("");
        }
    });
}