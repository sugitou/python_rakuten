// rakutenAPI関数
async function rakuten_func(kw_search, csv_name, box_name, select_api) {
    let val = await eel.rakuten_system(kw_search, csv_name, box_name, select_api)();
    for (let i = 0; i < val.length; i++) {
        let num = i + 1
        document.getElementById('com_name').value += "【" + num + "件目】" + val[i] + "\n";
    }
}

//初期表示はwrap02とwrap03を非表示
document.getElementById("wrap01").style.display ="block";
document.getElementById("wrap02").style.display ="none";
document.getElementById("wrap03").style.display ="none";
// 変数定義
const wrap01 = document.getElementById("wrap01").style.display;
const wrap02 = document.getElementById("wrap02").style.display;
const wrap03 = document.getElementById("wrap03").style.display;
// 切り替え関数
function vis_invis_01(){
    if(wrap01=="none"){
        // noneで非表示
        wrap01 ="block";
        wrap02 ="none";
        wrap03 ="none";
    }else{
        wrap01 ="block";
        wrap02 ="none";
        wrap03 ="none";
    }
}
function vis_invis_02(){
    if(wrap02=="none"){
        // noneで非表示
        wrap01 ="none";
        wrap02 ="block";
        wrap03 ="none";
    }else{
        wrap01 ="none";
        wrap02 ="block";
        wrap03 ="none";
    }
}
function vis_invis_03(){
    if(wrap03=="none"){
        // noneで非表示
        wrap01 ="none";
        wrap02 ="none";
        wrap03 ="block";
    }else{
        wrap01 ="none";
        wrap02 ="none";
        wrap03 ="block";
    }
}

let search = document.getElementById('search')
search.addEventListener('click', () => {
    if (input_form.input_kw.value == "") {
        alert("キーワードを入力してください");
        return false;
    }else if(input_form.input_f.value == ""){
        alert("ファイル名を入力してください");
        return false;
    }else if(input_form.input_d.value == ""){
        alert("フォルダ名を入力してください");
        return false;
    }else {
        if (wrap01="block") {
            rakuten_func(kw_search.value, csv_name.value, box_name.value, "market_search");
            return true;
        }else if (wrap02="block") {
            rakuten_func(kw_search.value, csv_name.value, box_name.value, "books_search");
            return true;
        }else {
            rakuten_func(kw_search.value, csv_name.value, box_name.value, "travel_search");
            return true;
        }
    }
})