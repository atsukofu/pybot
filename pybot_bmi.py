def bmi_command(command):
    try:
        data = command.split()
        weight = float(data[1])
        height = float(data[2])
        height2 = (height/100) ** 2
        bmi = round(weight / height2, 2)
        response = 'BMI ハ {}デス'.format(bmi)
    except IndexError:
        response = '2ツノ値(身長 体重)ヲ指定シテクダサイ'
    except ValueError:
        response = '正シイ数字ヲ指定シテクダサイ'
    return response

    # try:
    #     data = command.split()
    #     weight = int(data[1])
    #     height = int(data[2])
    #     bmi = weight / height **
    #     response = 'BMI ハ {}デス'.format(bmi)
    #
    # return response
