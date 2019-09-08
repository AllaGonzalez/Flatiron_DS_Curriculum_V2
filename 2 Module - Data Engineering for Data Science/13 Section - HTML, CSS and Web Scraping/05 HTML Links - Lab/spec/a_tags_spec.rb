

RSpec.describe 'index.html' do
  it 'contains a <a> tag with the href attribute set to an absolute path' do
    a = parsed_html.search('a')[0]
    expect(a).to_not be_nil, "No <a> tag was found"
    expect(html_file_contents).to include('</a>'), "Don't forget to include a closing </a>"
    expect(a.attributes["href"]).to_not be_nil, "No href attribute was found on the first 'a' tag"
    expect(a.attributes["href"]).to match(/.com|.net|.org|.co|.us|.edu|.gov/) , "An absolute path (a full website URL) was not found on the first 'a' tag"
  end

  it 'contains a <a> tag with the href attribute set to a relative path' do
    a = parsed_html.search('a')[1]
    expect(a).to_not be_nil, "A second <a> tag was not found"
    expect(a.attributes["href"]).to_not be_nil, "No href attribute was found on the second 'a' tag"
    expect(a.attributes["href"]).to match(/.html/) , "The correct relative path (about.html) was not found on the second 'a' tag"
  end

  it 'contains a <a> tag that uses the target attribute' do
    a = parsed_html.search('a')[2]
    expect(a).to_not be_nil, "A third <a> tag was not found"
    expect(a.attributes["target"]).to_not be_nil, "No target attribute was found on the third 'a' tag"
    expect(a.attributes["target"]).to match(/_blank/) , "The target attribute must be set to '_blank' to open a new window when clicked"
  end

end
