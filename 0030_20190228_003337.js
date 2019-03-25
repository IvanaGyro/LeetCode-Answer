/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function(s, words) {
    if (words.length == 0) return [];
    
    var table = Array.apply(null, Array(s.length));
    table.forEach((val, idx, arr) => {
        arr[idx] = [];
    });
    
    var wordTable = {};
    var newWords = [];
    words.forEach((word) => {
        if (wordTable[word] === undefined) {
            wordTable[word] = 1;
            newWords.push(word);
            let idx = -word.length;
            while ((idx = s.indexOf(word, idx + 1)) !== -1) {
                table[idx].push(newWords.length-1);
            }
        } 
        else {
            ++wordTable[word];
        }   
    });
    words = newWords;

    var ans = [];
    var stateTemplate = [], stateSum = 0;
    words.forEach((word, idx) => {
        stateSum += wordTable[word];
        stateTemplate[idx] = wordTable[word];
    });
    
    
    table.forEach((val, idx, table) => {
        var findConcat = function (idx, state, stateSum) {
            if (idx >= table.length) return false;
            let val = table[idx];
            if (val.length === 0) return false;
            for (let wordPosition of val) {
                if (state[wordPosition] == 0) continue;
                --state[wordPosition];
                --stateSum;
                if (stateSum == 0) {
                    ++state[wordPosition];
                    return true;
                }
                let newIdx = idx + words[wordPosition].length;
                let result = findConcat(newIdx, state, stateSum);
                ++state[wordPosition];
                ++stateSum;
                if (result) return true;
            }
            return false;
        }
        
        if(findConcat(idx, stateTemplate, stateSum)) ans.push(idx);
    });
    
    return ans;
};