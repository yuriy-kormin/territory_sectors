from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import TableStyle, LongTable


def chunk_line(string, max_length):
    len_string = len(string)
    if len_string <= max_length:
        return string
    string = "\n".join(
        [string[pos:pos + max_length] for pos in
         range(0, len_string, max_length)]
    )
    return string


def make_house_header(house, notation=True):
    result = [[house.address]]
    row_count = 1
    if notation:
        result.append(['Подъезд', 'Этаж', 'Квартира', 'Как найти'])
        row_count += 1
    return result, row_count


def generate_house_body(house, max_length):
    result = []
    row_count = 0
    for flat in house.flat_set.all():
        result.append([
            flat.entrance,
            flat.floor,
            flat.number,
            chunk_line(flat.way_desc, max_length)
        ])
        row_count += 1
    return result, row_count


def generate_empty_rows(count):
    return [[''] * 4 for _ in range(count)]


def build_table_data(houses, add_rows_count, max_desc_length):
    result = []
    total_row_count = 0
    address_lines = []
    for house in houses:
        # add house header
        res, row_count = make_house_header(house)
        address_lines.append(total_row_count + 1)
        total_row_count += row_count
        result.extend(res)
        # add house body
        res, row_count = generate_house_body(house, max_desc_length)
        result.extend(res)
        total_row_count += row_count
        # add empty lines
        if house.for_search:
            result.extend(generate_empty_rows(20))
            total_row_count += 20
        else:
            result.extend(generate_empty_rows(add_rows_count))
            total_row_count += add_rows_count
    return result, address_lines, total_row_count


def print_tables(pdf, sector_instance):
    # data = [['' for i in range(4)] for j in range(42)]

    # table = Table(data, colWidths=[i * cm for i in (2.5, 2.5, 2.5, 11.5)],
    #               rowHeights=None)
    # pdf.setFont("Arial", 10)
    data, span_lines, total_lines = build_table_data(
        sector_instance.get_houses_into(), 2, max_desc_length=89)
    table = LongTable(data, colWidths=[i * cm for i in (2, 2, 2, 13)],
                      splitByRow=1, repeatRows=1)
    table_style = [
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-2, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        # ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        # ('SPAN', (0, 0), (-1, 0)),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]
    for line_number in span_lines:
        table_style.extend([
            ('SPAN', (0, line_number - 1), (-1, line_number - 1)),
            # ('FONTNAME', (0, line_number - 1), (-1, line_number - 1),
            #  'Arial-Bold'),
        ])
    # print(table_style)
    table.setStyle(TableStyle(table_style))
    x = cm
    y = A4[1] - 1 * cm - table.wrapOn(pdf, A4[0] - 2 * cm, A4[1] - 2 * cm)[1]
    table.drawOn(pdf, x, y)
