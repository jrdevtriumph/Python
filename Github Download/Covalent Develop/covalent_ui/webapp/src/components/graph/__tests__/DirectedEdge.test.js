/**
 * This file is part of Covalent.
 *
 * Licensed under the Apache License 2.0 (the "License"). A copy of the
 * License may be obtained with this software package or at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Use of this file is prohibited except in compliance with the License.
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { render } from '@testing-library/react'
import DirectedEdge from '../DirectedEdge'


describe('dialog box', () => {
  test('renders directed edge', () => {
    const { container } = render(<DirectedEdge />);
    expect(container.getElementsByClassName("react-flow__edge-path").length).toBe(1);
  })

  test("renders directed edge fill color",() =>{
    const { container } = render(<DirectedEdge NODE_TEXT_COLOR={'rgba(250, 250, 250, 0.6)'} />);
    expect(container.getElementsByClassName("react-flow__edge-path").length).toBe(1);
  })
})