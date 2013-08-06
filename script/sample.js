$(function(){
  $("#file_01").change(function(){
    $("#mask_file_01").val($("#file_01").val());
  });
  $("#mask_file_01").click(function(){
    $("#file_01").click();
  });
});