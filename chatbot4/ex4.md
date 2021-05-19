# chatbot4

## ここに統合
・Flaskと連携
・ログイン機能実装済み（DB）
・training.pyであらかじめ学習させておけば、何度も学習させる必要がない


@app.route("/delete/<int:id>/",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = studyuser.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return redirect(url_for("study"))