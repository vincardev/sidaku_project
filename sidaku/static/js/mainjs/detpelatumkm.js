
tambahpelat   = document.getElementById("tambahpelat")
editpelat     = document.getElementById("editpelat")
modalpelat    = document.getElementById("modalpelat")

nmpelat       = document.getElementById("id_nm_pelat")
tmptpelat     = document.getElementById("id_tmpt_pelat")
thnpelat      = document.getElementById("id_thn_pelat")

var strjson_pelat = []

modalpelat.addEventListener("click", function(){

    nmpelat.value = "";
    tmptpelat.value = "";
    thnpelat.value = "";

    $("#editpelat").hide();
    $("#tambahpelat").show();
});

tambahpelat.addEventListener("click", function(){

    data = {
        "id":"",
        "nm_pelat":nmpelat.value,
        "tmpt_pelat":tmptpelat.value,
        "thn_pelat":thnpelat.value,
    }

    strjson_pelat.push(data);
    ConvertToTablepelat();

    $("#pelatdata").text(JSON.stringify(strjson_pelat));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTablepelat(index){
    strjson_pelat.splice(index,1);
    ConvertToTablepelat();
    $("#pelatdata").text(JSON.stringify(strjson_pelat));
}


function EditTablepelat(index){
    
    nmpelat.value    = strjson_pelat[index].nm_pelat;
    tmptpelat.value  = strjson_pelat[index].tmpt_pelat;
    thnpelat.value   = strjson_pelat[index].thn_pelat;

    idxinput.value = index;

    $("#editpelat").show();
    $("#tambahpelat").hide();
}


function EditDatapelat(){

    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson_pelat[index].nm_pelat      = nmpelat.value;
    strjson_pelat[index].tmpt_pelat     = tmptpelat.value ;
    strjson_pelat[index].thn_pelat   = thnpelat.value  ;

    ConvertToTablepelat();
    $("#pelatdata").text(JSON.stringify(strjson_pelat));
}

function ConvertToTablepelat(){
    html ="";
    for (let i = 0; i < strjson_pelat.length; i++) {
        html += "<tr>";
        html +=   "<td id='nm_pelat-"+i+"'>"+ strjson_pelat[i].nm_pelat+"</td>";
        html +=   "<td id='tmpt_pelat-"+i+"'>"+ strjson_pelat[i].tmpt_pelat+"</td>";
        html +=   "<td id='thn_pelat-"+i+"'>"+ strjson_pelat[i].thn_pelat+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addpelat' data-bs-whatever='Edit Data'  onclick='EditTablepelat("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTablepelat("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-pelat").html(html);
}