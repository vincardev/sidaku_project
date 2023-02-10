
tambahmsndata   = document.getElementById("tambahmsndata")
editmsndata     = document.getElementById("editmsndata")
modalmsndata    = document.getElementById("modalmsndata")

nmmesin       = document.getElementById("id_nm_mesin")
descmesin     = document.getElementById("id_desc_mesin")
jmlmesin      = document.getElementById("id_jml_mesin")

var strjson_msndata = []

modalmsndata.addEventListener("click", function(){

    nmmesin.value = "";
    descmesin.value = "";
    jmlmesin.value = "";

    $("#editmsndata").hide();
    $("#tambahmsndata").show();
});

tambahmsndata.addEventListener("click", function(){

    data = {
        "id":"",
        "nm_mesin":nmmesin.value,
        "desc_mesin":descmesin.value,
        "jml_mesin":jmlmesin.value,
    }

    strjson_msndata.push(data);
    ConvertToTablemsndata();

    $("#datamesin").text(JSON.stringify(strjson_msndata));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTablemsndata(index){
    strjson_msndata.splice(index,1);
    ConvertToTablemsndata();
    $("#datamesin").text(JSON.stringify(strjson_msndata));
}


function EditTablemsndata(index){
    
    nmmesin.value    = strjson_msndata[index].nm_mesin;
    descmesin.value  = strjson_msndata[index].desc_mesin;
    jmlmesin.value   = strjson_msndata[index].jml_mesin;

    idxinput.value = index;

    $("#editmsndata").show();
    $("#tambahmsndata").hide();
}


function EditDatamsndata(){

    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson_msndata[index].nm_mesin      = nmmesin.value;
    strjson_msndata[index].desc_mesin     = descmesin.value ;
    strjson_msndata[index].jml_mesin   = jmlmesin.value  ;

    ConvertToTablemsndata();
    $("#datamesin").text(JSON.stringify(strjson_msndata));
}

function ConvertToTablemsndata(){
    html ="";
    for (let i = 0; i < strjson_msndata.length; i++) {
        html += "<tr>";
        html +=   "<td id='nm_mesin-"+i+"'>"+ strjson_msndata[i].nm_mesin+"</td>";
        html +=   "<td id='desc_mesin-"+i+"'>"+ strjson_msndata[i].desc_mesin+"</td>";
        html +=   "<td id='jml_mesin-"+i+"'>"+ strjson_msndata[i].jml_mesin+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addmsndata' data-bs-whatever='Edit Data'  onclick='EditTablemsndata("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTablemsndata("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-msndata").html(html);
}