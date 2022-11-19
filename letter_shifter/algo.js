class ShiftCipher {
    constructor(num) {
        this._num = num;
    }

    encrypt(txt_to_enc) {
        let txt = txt_to_enc;
        let txt_new = [];

        for (let i in txt) {
            if (txt[i].charCodeAt() >= 97 && txt[i].charCodeAt() <= 122) {
        
                if (txt[i].charCodeAt() + this._num > 122) {
                    txt_new.push(String.fromCharCode(64 + (txt[i].charCodeAt() - 122) + this._num));
                } else {
                    txt_new.push(String.fromCharCode(txt[i].charCodeAt() - 32 + this._num));
                }

            } else {
                txt_new.push(txt[i]);
            }
    
    
        }

        txt_new = txt_new.join('');
        return(txt_new);
    }

    decrypt(txt_to_enc) {
        let txt = txt_to_enc;
        let txt_new = [];

        for (let i in txt) {
            if (txt[i].charCodeAt() >= 65 && txt[i].charCodeAt() <= 90) {
        
                if (txt[i].charCodeAt() - this._num < 65) {
                    txt_new.push(String.fromCharCode(122 - (65 - (txt[i].charCodeAt() - this._num))));
                } else {
                    txt_new.push(String.fromCharCode(txt[i].charCodeAt() + 32 - this._num));
                }

            } else {
                txt_new.push(txt[i]);
            }
    
    
        }

        txt_new = txt_new.join('');
        return(txt_new);
    }


}

const chega = new ShiftCipher(4);
console.log(chega.encrypt('hello, fellas!'));
console.log(chega.decrypt('LIPPS, JIPPEW!'));

// referencia de codigos de caracteres: https://en.wikipedia.org/wiki/List_of_Unicode_characters