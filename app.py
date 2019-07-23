# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:32:44 2019

@author: armazumd
"""

from flask import Flask
from linkedin_api import Linkedin
from flask import jsonify
app = Flask(__name__)

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/connections', methods = ['POST'])
def postJsonHandler():
    content = request.get_json()
    api = Linkedin(content['email'],content['password'])
    tag=content['tag'].lower()
    keyword=content['keyword'].lower()
    connections=api.search_people(network_depth ='F',limit=10)
    querry=[]
    for item in connections:
      
      if (len(querry)>=5):
            break
      data = {}
      value = item['public_id']
      retrieve=api.get_profile(value)
      if (tag=='location'):
            if ('locationName' in retrieve):
                if ( keyword  in retrieve['locationName'].lower() ):
                    
                    name=retrieve['firstName']+' '+retrieve['lastName']
                    link='https://www.linkedin.com/in/'+item['public_id']+'/'
                    #imgr=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['rootUrl'] 
                    #imgi=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['artifacts'][1]['fileIdentifyingUrlPathSegment']
                    data['name'] = name
                    data['link']=link
                    data['initials']=''.join(letter[0].upper() for letter in name.split())
                    data['info']=retrieve['summary']
                    #data['img']=imgr+imgi
                    querry.append(data)
      elif (tag=='company'):
            if ('experience' in retrieve):
                 if ( keyword in retrieve['experience'][0]['companyName'].lower()  ):
                     name=retrieve['firstName']+' '+retrieve['lastName']
                     link='https://www.linkedin.com/in/'+item['public_id']+'/'
                     #imgr=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['rootUrl'] 
                     #imgi=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['artifacts'][1]['fileIdentifyingUrlPathSegment']
                     data['name'] = name
                     data['link']=link
                     data['initials']=''.join(letter[0].upper() for letter in name.split())
                     data['info']=retrieve['summary']
                     #data['img']=imgr+imgi
                     querry.append(data)
      elif (tag=='title'):
            if ('experience' in retrieve):
                 if ( keyword in retrieve['experience'][0]['title'].lower()  ):
                     name=retrieve['firstName']+' '+retrieve['lastName']
                     link='https://www.linkedin.com/in/'+item['public_id']+'/'
                     #imgr=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['rootUrl'] 
                     #imgi=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['artifacts'][1]['fileIdentifyingUrlPathSegment']
                     data['name'] = name
                     data['link']=link
                     data['initials']=''.join(letter[0].upper() for letter in name.split())
                     data['info']=retrieve['summary']
                     #data['img']=imgr+imgi
                     querry.append(data)
      elif (tag=='skills'):
            if ('Skills' in retrieve):
                skillist=retrieve['Skills']
                if  any(keyword in s.lower() for s in skillist[1:]):
                    name=retrieve['firstName']+' '+retrieve['lastName']
                    link='https://www.linkedin.com/in/'+item['public_id']+'/'
                    #imgr=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['rootUrl'] 
                    #imgi=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['artifacts'][1]['fileIdentifyingUrlPathSegment']
                    data['name'] = name
                    data['link']=link
                    data['initials']=''.join(letter[0].upper() for letter in name.split())
                    data['info']=retrieve['summary']
                    #data['img']=imgr+imgi
                    querry.append(data)
                
      else:
          name=retrieve['firstName']+' '+retrieve['lastName']
          
          link='https://www.linkedin.com/in/'+item['public_id']+'/'
          #imgr=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['rootUrl'] 
          #imgi=retrieve['profilePictureOriginalImage']['com.linkedin.common.VectorImage']['artifacts'][1]['fileIdentifyingUrlPathSegment']
          data['name'] = name
          data['link']=link
          data['initials']=''.join(letter[0].upper() for letter in name.split())
          if ('summary' in retrieve):
              data['info']=retrieve['summary']
          #data['img']=imgr+imgi
          querry.append(data)
    
    return jsonify(querry)
  

if __name__ == '__main__':
    app.run(debug=True)

        
    
    