from conftest import get_zip_data


def test_pdf():
    zip_data = get_zip_data('pdf')
    print(f'zip_data = {zip_data}')

    assert zip_data is not None, 'Файл пустой'
    assert len(zip_data) == 2543, 'Некорректное количество символов'
    assert 'Similarly, a child or baby whose identity is unknown may be referred to as Baby Doe.' in zip_data,\
        'Строка не содержится в файле'


def test_xlsx():
    zip_data = get_zip_data('xlsx')
    print(f'zip_data = {zip_data}')

    assert zip_data is not None, 'Файл пустой'
    assert len(zip_data) == 648, 'Некорректное количество символов'
    assert 'Attribution-ShareAlike 3.0 Unported' in zip_data, 'Строка не содержится в файле'


def test_csv():
    zip_data = get_zip_data('csv')
    print(f'\n\nzip_data = \n\n{zip_data}')

    assert zip_data is not None, 'Файл пустой'
    assert len(zip_data) == 735, 'Некорректное количество символов'
    assert 'January,$5,00,$5,00,$7,00,$25,00,$42,00' in zip_data, 'Строка не содержится в файле'

