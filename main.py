import streamlit as st


st.title('Client Risk Analysis ')

st.subheader('''SCALE OF IMPORTANCE:
Less Important:10 \n
Averagely Important:50 \n
Very Important:100 \n ''')

st.header('NAME')
name=st.text_input('Name of the client:')

st.header('AGE')
age=st.number_input(' Age of the client :')
if age<30:
  risk1=30
elif age>=30:
  risk1=20
elif age>=50:
  risk1=10
weightage_age=st.radio('How important is age as a factor?', (10,50,100), index=0,key=int)
agee=risk1*(weightage_age)

st.header('HORIZON')
horizon=st.number_input('Investment Horizon of the client')
if horizon<5:
  risk2=10
elif horizon<10:
  risk2=20
elif horizon>=10:
  risk2=30
weightage_horizon=st.radio('How important is time horizon as a factor?', (10,50,100), index=0, key=int)
horizonn=risk2*(weightage_horizon)


st.header('GOALS')
goals=st.radio('How flexible are goals of client?',('not flexible','somewhat flexible','very flexible'), index=0,  key=int)
if goals=='not flexible':
  risk3=10
elif goals=='somewhat flexible':
  risk3=20
elif goals=='very flexible':
  risk3=30
weightage_goals=st.radio('How important are goals as a factor?', (10,50,100), index=0, key=int)
goalss=risk3*(weightage_goals)


st.header('EDUCATION')
risk_market=st.radio('How well versed is the client with the risks associated with the financial market?',('not well versed','somewhat well versed','very well versed'),index=0,  key=int)

if risk_market=='not well versed':
  risk4=10
elif risk_market=='somewhat well versed':
  risk4=20
elif risk_market=='very well versed':
  risk4=30
weightage_rwm=st.radio('How important is education as a factor?', (10,50,100), index=0, key=int)
risk_associated_w_mkt=risk4*(weightage_rwm)


st.header('STABLE INCOME')
stable_income=st.radio("How stable are the client's income sources?",("unstable","somewhat stable",'very stable'), index=0, key=int)
if stable_income=="unstable":
  risk5=10
elif stable_income=="somewhat stable":
  risk5=20
elif stable_income=='very stable':
  risk5=30
weightage_si=st.radio('How important is stable income as a factor?', (10,50,100), index=0, key=int)
stable_incomee=risk5*(weightage_si)


st.header('LOSS MITIGATION')
loss=st.radio('How would the client react too losses?',
('would prefer cut all losses immediately',
'would prefer giving investment some more time',
'would prefer holding on to stocks for the long term'), index=0, key=int)

if loss=='would prefer cut all losses immediately':
    risk6=10
elif loss=='would prefer giving investment some more time':
    risk6=20
elif loss=='would prefer holding on to stocks for the long term':
    risk6=30
weightage_ls=st.radio('How important is loss mitigation a factor?',(10,50,100), index=0, key=int)

loss_r=risk6*(weightage_ls)

total_conse=((weightage_age)*10)+((weightage_goals)*10)+((weightage_horizon)*10)+((weightage_si)*10)+((weightage_ls))*10+((weightage_rwm)*10)
total_moder=((weightage_age)*20)+((weightage_goals)*20)+((weightage_horizon)*20)+((weightage_si)*20)+((weightage_ls))*20+((weightage_rwm)*20)
total_aggre=((weightage_age)*30)+((weightage_goals)*30)+((weightage_horizon)*30)+((weightage_si)*30)+((weightage_ls))*30+((weightage_rwm)*30)
total=agee+horizonn+goalss+risk_associated_w_mkt+stable_incomee+loss_r
total_modag=(((total_aggre-total_moder)/2)+total_moder)
total_cc=total_conse+((total_aggre-total_conse)/5)
total_cm=total_cc+((total_aggre-total_conse)/5)
total_m=total_cm+((total_aggre-total_conse)/5)
total_ma=total_m+((total_aggre-total_conse)/5)
total_a=total_ma+((total_aggre-total_conse)/5)


st.header('RISK APPETITE')
if total<total_conse:
  st.info('try again')
elif total<total_cc:
  st.info('The risk appetite of the client is Conservative')
elif total<total_cm:
  st.info(' The risk appetite of  is Moderately Conservative')
elif total<total_m:
  st.subheader(' The risk appetite of the client is Moderate \n ')
elif total<total_ma:
  st.info(' The risk appetite of the client is Moderately Aggressive')
elif total<total_a:
  st.info('The risk appetite of the client is Aggressive')


st.write('                      ~ Client risk analysis  by Cartography of Investments')
