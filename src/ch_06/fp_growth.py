"""
Frequent Pattern Growth (FP-Growth): Mining Frequent Patterns
"""
import numpy as np
import pandas as pd
import pyfpgrowth as fp


dict1 = {
    'id':[0,1,2,3],
    'items':[
        ["wickets","pads"],
        ["bat","wickets","pads","helmet"],
        ["helmet","pad"],
        ["bat","pads","helmet"]
    ]
}

transactionSet = pd.DataFrame(dict1)

patterns = fp.find_frequent_patterns(transactionSet['items'], 1)


if __name__ == '__main__':
    print(patterns)

    rules = fp.generate_association_rules(patterns, 0.3)
    print(rules)
