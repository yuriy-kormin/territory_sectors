function hide_show_completed_rows(){
    var button = document.getElementById("toggle");
    const rows = document.querySelectorAll('tr');


    if (button.classList.contains('show')){
        rows.forEach((row) => {
            if (row.classList.contains('d-none')) {
                row.classList.remove('d-none');
            }
        })
        button.classList.remove('show');
        button.textContent="Hide completed"
    } else {
        rows.forEach(function(row) {
            if (row.classList.contains('hidden')) {
                row.classList.add('d-none');
            }
        })
        button.classList.add('show');
        button.textContent="Show all"

        // for (var i = 0, row; row = table.rows[i]; i++) {
        //     if ('d-none' in row.classList) {
        //         row.classList.add('d-none')
        //     }
        // }
        // button.classList.add('show')
    }
}