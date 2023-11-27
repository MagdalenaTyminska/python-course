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

html = HTML(string=string)
html.write_pdf('test.pdf')