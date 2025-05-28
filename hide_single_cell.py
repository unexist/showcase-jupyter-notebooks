from IPython.display import HTML
from IPython.display import display

# Taken from https://stackoverflow.com/questions/31517194/how-to-hide-one-specific-cell-input-or-output-in-ipython-notebook
tag = HTML('''<script>
code_show=true;
function code_toggle() {
    if (code_show) {
        $('div.cell.code_cell.rendered.selected div.input').hide();
    } else {
        $('div.cell.code_cell.rendered.selected div.input').show();
    }

    code_show = !code_show
}

code_toggle();
</script>
Der Code dieser Zelle ist ausgeblendet, <a href="javascript:code_toggle()">hier</a> klicken um diesen ein- bzw wieder auszublenden.''')
display(tag)
