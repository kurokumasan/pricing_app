def get_int(x:float) -> int:
    return int(x) if x%10==0 else (int(x)//10+1)*10

def price_estimation(cost:int, host:int, host_no:int, guests:int, songs:int, group:int=5, guest_stage:int=2, place:str='表演場地'):
    
    try:
        all_stages = group * songs
        cost_per_song = cost / all_stages
        guest_cost = guest_stage * cost_per_song
        host_stages = all_stages - guest_stage * guests
        host_cost = cost - guest_cost * guests
    
        host_cost_per_song = host_cost / (host_stages + 1.5*host_no)
        host_cost_without_stage = 1.5*host_cost_per_song
        host_avg_stages = host_stages / (host-host_no)
        host_avg_stage_cost = host_cost_per_song * host_avg_stages
    
        income = get_int(host_cost_per_song)*host_stages+get_int(host_cost_without_stage)*host_no+get_int(guest_cost)*guests

        if (host_avg_stages==int(host_avg_stages)):
            result = f"\
    估算方案：{place}\n\
        【主辦】\n\
        上台：{host_cost_per_song:.4f}(元/首)\n\
            平均接歌數量：{host_avg_stages:.4f}(首/人)\n\
            平均付費金額：{host_avg_stage_cost:.4f}(元/人)\n\
            沒上台：{host_cost_without_stage:.4f}(元/人)\n\
        【協辦】\n\
            {guest_cost:.4f}(元/人)\n\
    \n\
    *********以下數據以10為基本單位取整數*********\n\n\
        【主辦】\n\
            上台：{get_int(host_cost_per_song)}(元/首)\n\
            平均接歌數量：{int(host_avg_stages)}(首/人)\n\
            平均付費金額：{int(host_avg_stages)*get_int(host_cost_per_song)}(元/人)\n\
            沒上台：{get_int(host_cost_without_stage)}(元/人)\n\
        【協辦】\n\
            {get_int(guest_cost)}(元/人)\n\
        成本為{cost}元，總共收{income}元，最後會多出{income-cost}元納入社費"
            return result, (place, f'{get_int(host_cost_per_song)}', f'{int(host_avg_stages)}', f'{int(host_avg_stages)*get_int(host_cost_per_song)}', f'{get_int(host_cost_without_stage)}', f'{get_int(guest_cost)}')
        else:
            result = f"\
    估算方案：{place}\n\
        【主辦】\n\
            上台：{host_cost_per_song:.4f}(元/首)\n\
            平均接歌數量：{host_avg_stages:.4f}(首/人)\n\
            平均付費金額：{host_avg_stage_cost:.4f}(元/人)\n\
            沒上台：{host_cost_without_stage:.4f}(元/人)\n\
        【協辦】\n\
            {guest_cost:.4f}(元/人)\n\
    \n\
    *********以下數據以10為基本單位取整數*********\n\n\
        【主辦】\n\
            上台：{get_int(host_cost_per_song)}(元/首)\n\
            平均接歌數量：{int(host_avg_stages)}到{int(host_avg_stages)+1}(首/人)\n\
            平均付費金額：{int(host_avg_stages)*get_int(host_cost_per_song)}到{(int(host_avg_stages)+1)*get_int(host_cost_per_song)}(元/人)\n\
            沒上台：{get_int(host_cost_without_stage)}(元/人)\n\
        【協辦】\n\
            {get_int(guest_cost)}(元/人)\n\
        成本為{cost}元，總共收{income}元，最後會多出{income-cost}元納入社費"
            return result, (place, f'{get_int(host_cost_per_song)}', f'{int(host_avg_stages)}-{int(host_avg_stages)+1}', f'{int(host_avg_stages)*get_int(host_cost_per_song)}-{(int(host_avg_stages)+1)*get_int(host_cost_per_song)}', f'{get_int(host_cost_without_stage)}', f'{get_int(guest_cost)}')
    except:
        return 'Invalid input'
    
def price_detailed(cost:int, host:int, host_no:int, guests:int, all_stages:int, guest_stages:int, place:str='表演場地'):
    
    try:
        host_stages = all_stages - guest_stages
        cost_per_song = cost / all_stages
        guest_cost = round(guest_stages/guests) * cost_per_song
        host_cost = cost - guest_cost * guests
    
        host_cost_per_song = host_cost / (host_stages + 1.5*host_no)
        host_cost_without_stage = 1.5*host_cost_per_song
        host_avg_stages = host_stages / (host-host_no)
        host_avg_stage_cost = host_cost_per_song * host_avg_stages
    
        income = get_int(host_cost_per_song)*host_stages+get_int(host_cost_without_stage)*host_no+get_int(guest_cost)*guests

        if (host_avg_stages==int(host_avg_stages)):
            result = f"\
    精算方案：{place}\n\
        【主辦】\n\
            上台：{host_cost_per_song:.4f}(元/首)\n\
            平均接歌數量：{host_avg_stages:.4f}(首/人)\n\
            平均付費金額：{host_avg_stage_cost:.4f}(元/人)\n\
            沒上台：{host_cost_without_stage:.4f}(元/人)\n\
        【協辦】\n\
            {guest_cost:.4f}(元/人)\n\
            平均上台次數：{guest_stages/guests:.4f}，四捨五入取{round(guest_stages/guests)}次\n\
    \n\
    *********以下數據以10為基本單位取整數*********\n\n\
        【主辦】\n\
            上台：{get_int(host_cost_per_song)}(元/首)\n\
            平均接歌數量：{int(host_avg_stages)}(首/人)\n\
            平均付費金額：{int(host_avg_stages)*get_int(host_cost_per_song)}(元/人)\n\
            沒上台：{get_int(host_cost_without_stage)}(元/人)\n\
        【協辦】\n\
            {get_int(guest_cost)}(元/人)\n\
        成本為{cost}元，總共收{income}元，最後會多出{income-cost}元納入社費"

        else:
            result = f"\
    精算方案：{place}\n\
        【主辦】\n\
            上台：{host_cost_per_song:.4f}(元/首)\n\
            平均接歌數量：{host_avg_stages:.4f}(首/人)\n\
            平均付費金額：{host_avg_stage_cost:.4f}(元/人)\n\
            沒上台：{host_cost_without_stage:.4f}(元/人)\n\
        【協辦】\n\
            {guest_cost:.4f}(元/人)\n\
            平均上台次數：{guest_stages/guests:.4f}，四捨五入取{round(guest_stages/guests)}次\n\
    \n\
    *********以下數據以10為基本單位取整數*********\n\n\
        【主辦】\n\
            上台：{get_int(host_cost_per_song)}(元/首)\n\
            平均接歌數量：{int(host_avg_stages)}到{int(host_avg_stages)+1}(首/人)\n\
            平均付費金額：{int(host_avg_stages)*get_int(host_cost_per_song)}到{(int(host_avg_stages)+1)*get_int(host_cost_per_song)}(元/人)\n\
            沒上台：{get_int(host_cost_without_stage)}(元/人)\n\
        【協辦】\n\
            {get_int(guest_cost)}(元/人)\n\
        成本為{cost}元，總共收{income}元，最後會多出{income-cost}元納入社費"
    	
        return result
    except Exception as e:
        return 'Invalid input'

