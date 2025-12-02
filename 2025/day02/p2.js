import { readFileSync } from 'fs';

function isRepeating(str, pattern) {
    if (str.length % pattern.length !== 0) return false;
    while (str) {
        const p1 = str.substring(0, pattern.length);
        const p2 = str.substring(pattern.length, pattern.length * 2);
        
        if (!p2 || p1 === p2) {
            str = str.slice(pattern.length);
            continue;
        }

        return false;
    }

    return true;
}


function main() {
    const buffer = readFileSync('input', 'utf8');
    const productIds = buffer.split(',');
    
    let sum = 0;
    for (let id of productIds) {
        const [start, end] = id.split('-').map(Number);
        
        for (let i = start; i <= end; i++) {
            const idStr = `${i}`;
            
            let foundMatch = false;
            for (let k = 0; k <= Math.floor(idStr.length / 2); k++) {
                const pattern = idStr.substring(0, k);
                if (isRepeating(idStr, pattern)) {
                    console.log(`${idStr} is repeating ${pattern}`);
                    sum += i;
                    foundMatch = true;
                    break;
                }
            }

            if (foundMatch) {
                continue;
            }
        }
    }

    console.log(sum);
}

main();