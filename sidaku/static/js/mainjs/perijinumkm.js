
tambahijin   = document.getElementById("tambahijin")
editijin     = document.getElementById("editijin")
modalijin    = document.getElementById("modalijin")

tpijin       = document.getElementById("id_tipe_ijin")
noijin       = document.getElementById("id_no_ijin")
tglijin      = document.getElementById("id_tgl_ijin")

var strjson_ijin = []

modalijin.addEventListener("click", function(){

    tpijin.value = "";
    noijin.value = "";
    tglijin.value = "";

    $("#editijin").hide();
    $("#tambahijin").show();
});

tambahijin.addEventListener("click", function(){

    data = {
        "id":"",
        "tipe_ijin":tpijin.value,
        "no_ijin":noijin.value,
        "tgl_ijin":tglijin.value,
    }

    strjson_ijin.push(data);
    ConvertToTableIjin();

    $("#dataijin").text(JSON.stringify(strjson_ijin));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTableIjin(index){
    strjson_ijin.splice(index,1);
    ConvertToTableIjin();
    $("#dataijin").text(JSON.stringify(strjson_ijin));
}


function EditTableIjin(index){
    
    tpijin.value    = strjson_ijin[index].tipe_ijin;
    noijin.value  = strjson_ijin[index].no_ijin;
    tglijin.value     = strjson_ijin[index].tgl_ijin;

    idxinput.value = index;

    $("#editijin").show();
    $("#tambahijin").hide();
}


function EditDataIjin(){

    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson_ijin[index].tipe_ijin      = tpijin.value;
    strjson_ijin[index].no_ijin     = noijin.value ;
    strjson_ijin[index].tgl_ijin   = tglijin.value  ;

    ConvertToTableIjin();
    $("#dataijin").text(JSON.stringify(strjson_ijin));
}

function ConvertToTableIjin(){
    html ="";
    for (let i = 0; i < strjson_ijin.length; i++) {
        html += "<tr>";
        html +=   "<td id='tipe_ijin-"+i+"'>"+ strjson_ijin[i].tipe_ijin+"</td>";
        html +=   "<td id='no_ijin-"+i+"'>"+ strjson_ijin[i].no_ijin+"</td>";
        html +=   "<td id='tgl_ijin-"+i+"'>"+ strjson_ijin[i].tgl_ijin+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addijin' data-bs-whatever='Edit Data'  onclick='EditTableIjin("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTableIjin("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-ijin").html(html);
}