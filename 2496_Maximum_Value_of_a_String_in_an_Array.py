for i in range(0, len(strs)):
            if strs[i].isdigit():
                d.append(int(strs[i]))
            else:
                d.append(len(strs[i]))
        return (max(d))
