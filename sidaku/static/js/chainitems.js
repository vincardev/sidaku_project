function OnChangeStock(status) {
    // console.log($("#boolstock").val());
    if (status == "True") {
        $("#inputstock").attr("readonly", false);
    } else {

        $("#inputstock").attr("readonly", true);
        $("#inputstock").val(0);
    }
}


function OnSpecificDate(status){

    $("#ritemid").hide();
    $("label[for='ritemid']").hide();

    $("#rroomid").hide();
    $("label[for='rroomid']").hide();

    $("#rpackid").hide();
    $("label[for='rpackid']").hide();
    
    if (status == "True") {
        $("#nrmrate1").hide();
        $("#nrmrate1").val(0);
        $("label[for='nrmrate1']").hide();
        $("#nrmrate2").hide();
        $("#nrmrate2").val(0);
        $("label[for='nrmrate2']").hide();

        $("#spcrate1").show();
        $("label[for='spcrate1']").show();
        $("#spcrate2").show();
        $("label[for='spcrate2']").show();
    } else {
        $("#nrmrate1").show();
        $("label[for='nrmrate1']").show();
        $("#nrmrate2").show();
        $("label[for='nrmrate2']").show();

        $("#spcrate1").hide();
        $("#spcrate1").val(0);
        $("label[for='spcrate1']").hide();
        $("#spcrate2").hide();
        $("#spcrate2").val(0);
        $("label[for='spcrate2']").hide();
    }
}