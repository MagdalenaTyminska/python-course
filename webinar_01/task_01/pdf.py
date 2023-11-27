from weasyprint import HTML, CSS

string = '''<table>
    <thead>
        <tr>
            <th>Pracownik</th>
            <th>Czas pracy</th>
        </tr>
    <thead>
    <tbody>
        <tr>
            <td>Mateusz</td>
            <td>10h 30min</td>
        </tr>
    </body>
</table>'''

stylesheet = '''
    body {
        font-family: sans-serif;
    }
    thread tr {
        border-bottom: 3px solid black;
    }
    tbody td {
        border-bottom: 1px solid black;
    }
    tbody tr td {
        padding-bottom: 5px;
    }
'''

html = HTML(string=string)
css = CSS(string=stylesheet)
html.write_pdf('test.pdf', stylesheets=[css])