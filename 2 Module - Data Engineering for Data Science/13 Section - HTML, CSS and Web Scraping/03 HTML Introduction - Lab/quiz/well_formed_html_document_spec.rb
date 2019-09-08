RSpec.describe "Well-Formed HTML Document" do
  it 'begins with a valid doctype' do
    expect(parsed_html.children.first).to be_html5_dtd
  end

  it 'has a top-level <html> tag to enclose the document' do
    expect(parsed_html.child.name).to match(/html/i)

    expect(html_file_contents).to include('<html>')
    expect(html_file_contents).to include('</html>')
  end

  context 'within <html>' do
    it 'contains a <head> tag to enclose the header' do
      head = parsed_html.search('html > head').first

      expect(head.name).to eq('head')

      expect(html_file_contents).to include('</head>')
    end

    context 'within <head>' do
      it 'contains a <title> tag to enclose the site title' do
        title = parsed_html.search('html > head > title').first

        expect(title.name).to eq('title')

        expect(html_file_contents).to include('</title>')
      end
    end
  end

  context 'within <html>' do
    it 'contains a <body> tag to enclose the body of the document' do
      body = parsed_html.search('html > body').first

      expect(body.name).to eq('body')

      expect(html_file_contents).to include('</body>')
    end
  end

  context 'w3c validation' do
    it 'is a valid w3c document' do
      validator = W3CValidators::NuValidator.new
      html = File.read('./index.html')
      results = validator.validate_text(html)

      error_messages = "Expected a valid w3c document but got:\n#{results.errors.collect{|e| e.to_s}.join("\n")}"

      expect(results.errors).to be_empty, error_messages
    end
  end
end
