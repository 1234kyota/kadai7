translate_btn.addEventListener('click', () => {
    if (trans_src.value != "") {
        eel.context_translate(trans_src.value,before_translate.value,after_translate.value);
    } else {
        alert("翻訳したい文章を入力してください");
    }
})

eel.expose(view_result)
function view_result(context){
    trans_dest.value = context;
}