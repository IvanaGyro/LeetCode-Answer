/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    var roman = '';
    var tb = [
        ['M', 'D', 'C'],
        ['C', 'L', 'X'],
        ['X', 'V', 'I']
    ];
    while (num >= 1000) {
        roman += 'M';
        num -= 1000;
    }
    var mask = 100;
    for (var i = 0; i < 3; ++i) {
        var digit = (num - num % mask)/mask;
        num %= mask;
        if (digit == 9) {
            roman = roman + tb[i][2] + tb[i][0];
        } else {
            if (digit == 4) {
                roman = roman + tb[i][2] + tb[i][1];
            } else {
                if (digit >= 5) {
                    roman += tb[i][1];
                    digit -= 5;
                }
                while (digit--) {
                    roman += tb[i][2];
                }
            }
        }
        mask /= 10;
    }
    return roman;
};