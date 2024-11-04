def compare_files(file1, file2):
    # file2 첫번째 컬럼과 같은 게 있는지 확인
    same_lines = []
    
    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            
            same_request = {}
            for line1 in f1:
                for line2 in f2:
                   uid_source = line1.replace('\n', '').replace('"', '')
                   uid_target = line2.split(', ')[0].replace('"', '')
                   
                   if uid_source == uid_target:
                        uid = uid_source
                        request = line2.split(', ')[1].replace('\n', '')
                        same_request = {
                            uid : int(request)
                        }
                        
                        same_lines.append(same_request)
                f2.seek(0)  # f2 파일을 다시 처음으로 돌려놓기
                
    return same_lines

# Example usage
file1 = 'ifa/ifa'
file2 = 'dailyuser/ifa_request'
same_lines = compare_files(file1, file2)
print(same_lines)